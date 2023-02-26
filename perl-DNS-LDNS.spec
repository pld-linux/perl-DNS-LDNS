#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	DNS
%define		pnam	LDNS
Summary:	DNS::LDNS - Perl extension for the ldns library
Summary(pl.UTF-8):	DNS::LDNS - rozszerzenie Perla do biblioteki ldns
Name:		perl-DNS-LDNS
Version:	0.63
Release:	2
# same as perl 5.14.2+ (see LDNS.pm; LICENSE is old and misleading)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DNS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c544481a56995b1abcb70405e9e26877
URL:		https://metacpan.org/release/DNS-LDNS
BuildRequires:	ldns-devel
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.14.2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DNS::LDNS is a Perl OO-wrapper for the ldns library. A complete list
of object methods is found in the perldoc for each of the individual
classes. You may also read the documentation of the ldns library
<https://www.nlnetlabs.nl/projects/ldns/about/>.

%description -l pl.UTF-8
DNS::LDNS to obiektowy interfejs perlowy do biblioteki ldns. Pełna
lista metod jest dostępna w dokumentacji każdej klasy. Dokumentację
biblioteki ldns można znaleźć pod adresem
<https://www.nlnetlabs.nl/projects/ldns/about/>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__rm} t/{dnssec_datachain,resolver}.t

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/DNS
%{perl_vendorarch}/DNS/LDNS.pm
%{perl_vendorarch}/DNS/LDNS
%dir %{perl_vendorarch}/auto/DNS
%dir %{perl_vendorarch}/auto/DNS/LDNS
%attr(755,root,root) %{perl_vendorarch}/auto/DNS/LDNS/LDNS.so
%{perl_vendorarch}/auto/DNS/LDNS/autosplit.ix
%{_mandir}/man3/DNS::LDNS*.3pm*
